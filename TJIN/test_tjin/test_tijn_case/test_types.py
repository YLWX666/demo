import unittest
from element_step.step import StepElement


class TestTypes(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = StepElement()
        self.driver.open_url('https://tj.qa.heywind.cn/')

    def tearDown(self) -> None:
        self.driver.close_web()


    def test_optical(self):
        optical = self.driver.types_optical(2)
        self.assertTrue(optical)


    def test_blue(self):
        blue = self.driver.types_blue(2)
        self.assertTrue(blue)

    def test_story(self):
        story = self.driver.type_story(2)
        self.assertTrue(story)

    def test_sunwear(self):
        sunwear = self.driver.type_sunwear(2)
        self.assertTrue(sunwear)

    def test_prescription(self):
        prescription = self.driver.type_prescription(2)
        self.assertTrue(prescription)

    def test_life(self):
        life = self.driver.type_life(2)
        self.assertTrue(life)

    def test_eco(self):
        eco = self.driver.type_eco(2)
        self.assertTrue(eco)

    def test_pets(self):
        pets = self.driver.type_pets(2)
        self.assertTrue(pets)

    def test_search(self):
        search = self.driver.type_search(2)
        self.assertEqual(search,'Search TIJN')


# if __name__ == "__main__":
#     unittest.main()


















