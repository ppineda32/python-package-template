from mypythonlib import myfunctions


def test_haversine():
    value = myfunctions.haversine(52.370216, 4.895168, 52.520008,
    13.404954)
    assert value["result"] == 946.3876221719836
    assert value["status"] == "success"