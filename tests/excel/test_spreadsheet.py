import io
import sys
import unittest

from koala.Spreadsheet import *
sys.setrecursionlimit(3000)

class Test_Spreadsheet(unittest.TestCase):
    # TODO: At the moment Spreadsheet() means nothing. Maybe an empty "cellmap" or ExcelCompiler? OR mock.
    # def test_create_evaluate_update(self):
    #     spreadsheet = Spreadsheet()
    #
    #     spreadsheet.cell_add('Sheet1!A1', value=1)
    #     spreadsheet.cell_add('Sheet1!A2', value=2)
    #     spreadsheet.cell_add('Sheet1!A3', formula='=SUM(Sheet1!A1, Sheet1!A2)')
    #     spreadsheet.cell_add('Sheet1!A4', formula='=SUM(Sheet1!A1:A2)')
    #     spreadsheet.cell_add('Sheet1!A5', formula='=SUM(Sheet1!A1:A1)')
    #
    #     self.assertEqual(spreadsheet.evaluate('Sheet1!A3'), 3)  # test function
    #     self.assertEqual(spreadsheet.evaluate('Sheet1!A4'), 3)  # test range
    #     self.assertEqual(spreadsheet.evaluate('Sheet1!A5'), 1)  # test short range
    #
    #     spreadsheet.set_value('Sheet1!A2', 10)
    #
    #     self.assertEqual(spreadsheet.evaluate('Sheet1!A3'), 11)  # test function
    #     self.assertEqual(spreadsheet.evaluate('Sheet1!A4'), 11)  # test range
    #     self.assertEqual(spreadsheet.evaluate('Sheet1!A5'), 1)  # test short range


    def test_load_filename(self):
        spreadsheet = Spreadsheet.from_file_name("./tests/excel/VDB.xlsx")
        # really just testing the loading from "fin", but check one cell to be sure it read
        self.assertEqual(spreadsheet.evaluate('Sheet1!A2'), "Init")


    def test_load_stream(self):
        spreadsheet = Spreadsheet.build_spreadsheet("./tests/excel/VDB.xlsx")
        self.assertEqual(spreadsheet.evaluate('Sheet1!A2'), "Init")


    def test_as_from_dict(self):
        sp1 = Spreadsheet.build_spreadsheet("./tests/excel/VDB.xlsx")
        sp1.cell_set_value('Sheet1!B7', 100)
        sp1.cell_set_value('Sheet1!B8', 200)
        # serialize to a dict, then back to a clone instance
        data = sp1.asdict()
        sp2 = Spreadsheet.from_dict(data)
        # set values in the new spreadsheet - should be different than before
        sp2.cell_set_value('Sheet1!B7', 500)
        sp2.cell_set_value('Sheet1!B8', 600)
        self.assertNotEqual(sp1.evaluate('Sheet1!B7'), sp2.evaluate('Sheet1!B7'))
        self.assertNotEqual(sp1.evaluate('Sheet1!B8'), sp2.evaluate('Sheet1!B8'))
