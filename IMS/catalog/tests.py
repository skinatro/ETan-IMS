from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Component, Order, OrderItem

User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@sfit.ac.in",
            password="testpass123",
            pid=12345,
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.pid, 12345)
        self.assertEqual(self.user.role, "customer")
        self.assertFalse(self.user.is_member)

    def test_user_str(self):
        self.assertEqual(str(self.user), "test@sfit.ac.in")

    def test_admin_role(self):
        admin = User.objects.create_user(
            username="admin1", password="adminpass1", role="admin"
        )
        self.assertEqual(admin.role, "admin")


class ComponentModelTest(TestCase):
    def setUp(self):
        self.component = Component.objects.create(
            name="Arduino Uno",
            category="MC",
            quantity=5,
            rental_rate=50,
        )

    def test_component_creation(self):
        self.assertEqual(self.component.name, "Arduino Uno")
        self.assertEqual(self.component.category, "MC")
        self.assertEqual(self.component.quantity, 5)
        self.assertTrue(self.component.is_rentable)

    def test_component_str(self):
        self.assertEqual(str(self.component), "Arduino Uno")


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="student", password="pass12345", pid=11111
        )
        self.component = Component.objects.create(
            name="Resistor 1K", quantity=100, rental_rate=5
        )
        self.order = Order.objects.create(user=self.user)
        self.item = OrderItem.objects.create(
            order=self.order, component=self.component, quantity=10
        )

    def test_order_default_status(self):
        self.assertEqual(self.order.status, "booked")

    def test_order_str(self):
        self.assertIn("Order #", str(self.order))

    def test_order_item(self):
        self.assertEqual(self.item.quantity, 10)
        self.assertEqual(str(self.item), "Resistor 1K x10")

    def test_order_item_unique(self):
        with self.assertRaises(Exception):
            OrderItem.objects.create(
                order=self.order, component=self.component, quantity=5
            )


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="student1", password="testpass123", pid=22222
        )
        self.admin = User.objects.create_user(
            username="admin1", password="adminpass1", role="admin"
        )
        self.component = Component.objects.create(
            name="LED Red", quantity=50, rental_rate=2
        )

    def test_inventory_list(self):
        response = self.client.get("/inventory/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "LED Red")

    def test_dashboard_requires_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_dashboard_logged_in(self):
        self.client.login(username="student1", password="testpass123")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard(self):
        self.client.login(username="admin1", password="adminpass1")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Dashboard")

    def test_component_detail(self):
        self.client.login(username="student1", password="testpass123")
        response = self.client.get(f"/inventory/{self.component.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "LED Red")

    def test_admin_create_component(self):
        self.client.login(username="admin1", password="adminpass1")
        response = self.client.get("/inventory/add/")
        self.assertEqual(response.status_code, 200)

    def test_customer_cannot_create_component(self):
        self.client.login(username="student1", password="testpass123")
        response = self.client.get("/inventory/add/")
        self.assertEqual(response.status_code, 403)

    def test_register(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
