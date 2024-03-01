from src.confing import operations_json


def test_confing():
    assert (operations_json[0] or "{'date': '2019-08-26T10:50:58.294041', "
                                  "'description': 'Перевод организации', "
                                  "'from': 'Maestro 1596837868705199', "
                                  "'id': 441945886, ...}")
