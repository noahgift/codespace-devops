from click.testing import CliRunner
from hello import search


def test_search():
    runner = CliRunner()
    result = runner.invoke(search, ["--path", ".", "--ftype", "py"])
    assert result.exit_code == 0
    assert ".py" in result.output
