from src.recommendationsystems import main


def test_main_prints_greeting(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from recommendationsystems!\n"
