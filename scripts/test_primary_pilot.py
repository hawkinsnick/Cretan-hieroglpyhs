import copy,json,unittest
from validate_primary_pilot import validate,R
class PilotTests(unittest.TestCase):
    def setUp(self):
        self.readings=json.loads((R/'corpus/critical-readings.json').read_text());self.report=json.loads((R/'analysis/chic-primary-pilot-v1.json').read_text())
    def test_known_pilot(self):self.assertEqual(validate(self.readings,self.report)['source_checked_readings'],5)
    def test_bad_reading_rejected(self):
        for mutation in ['id','mark','locator','phonetic','position']:
            r=copy.deepcopy(self.readings)
            if mutation=='id':r[0]['object_id']='CHIC-001'
            elif mutation=='mark':r[0]['tokens'].pop(0)
            elif mutation=='locator':r[0]['locator']='p. 93'
            elif mutation=='phonetic':r[0]['tokens'][1]['form']='pa'
            else:r[0]['tokens'][0]['position']=2
            with self.subTest(mutation=mutation),self.assertRaises(Exception):validate(r,self.report)
        report=copy.deepcopy(self.report);report['external_review_completed']=True
        with self.assertRaises(ValueError):validate(self.readings,report)
if __name__=='__main__':unittest.main()
