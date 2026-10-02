import sys
from pathlib import Path


def test_main_prints_expected_message(capsys):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from recommendationsystems import main

    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello from recommendationsystems!"
