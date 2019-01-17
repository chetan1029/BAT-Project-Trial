from django.test import TestCase
from settings.models import (Category, Color, Size, Status, Currency)
# Create your tests here.

class SettingsTestCase(TestCase):
    def setUp(self):
        product = Category.objects.create(name="Products")
        cable = Category.objects.create(name="Cable",parent=product)
        micro_usb_cable = Category.objects.create(name="Micro USB Cable",parent=cable)
        usb_c_cable = Category.objects.create(name="USB C Cable",parent=cable)
        lighting_cable = Category.objects.create(name="Lighting Cable",parent=cable)
        adpater = Category.objects.create(name="Adapter",parent=product)
        usb_a_to_usb_c_adpater = Category.objects.create(name="USB A to USB C Adapter",parent=adpater)
        micro_usb_to_usb_c_adpater = Category.objects.create(name="Micro USB to USB C Adapter",parent=adpater)

        product = Status.objects.create(title="Products")
        planning = Status.objects.create(title="Planning",parent=product)
        in_progress = Status.objects.create(title="In Progress",parent=planning)

        moss_green = Color.objects.create(name="Moss Green")
        ruby = Color.objects.create(name="Ruby")

        cm_30 = Size.objects.create(name="0.3M")
        m_1 = Size.objects.create(name="1M")

        usd = Currency.objects.create(title="USD")
        eur = Currency.objects.create(title="EUR")

    def test_category(self):
        cable = Category.objects.get(name="Cable")
        self.assertEqual(cable.name,"Cable")

        in_progress = Status.objects.get(title="In Progress")
        self.assertEqual(in_progress.title,"In Progress")

        ruby = Color.objects.get(name="Ruby")
        self.assertEqual(ruby.name,"Ruby")

        m_1 = Size.objects.get(name="1M")
        self.assertEqual(m_1.name,"1M")

        eur = Currency.objects.get(title="EUR")
        self.assertEqual(eur.title,"EUR")
