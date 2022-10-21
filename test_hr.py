import hr

def test_employeename_valid():
    assert hr.validate_employeename("andrew")

def test_employeename_tooshort():
    assert not hr.validate_employeename("an")

def test_employeename_toolong():
    assert not hr.validate_employeename("ansdfasdfsdfsd445345gsdfgsertsergsers")