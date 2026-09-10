import gzip
import subprocess
import sys
from pathlib import Path


def test_secret_scanner_checks_alias_credentials_inside_compressed_artifacts(tmp_path):
    script = Path(__file__).resolve().parents[1] / 'scripts/check_secrets.py'
    subprocess.run(['git', 'init', '-q', str(tmp_path)], check=True)
    fake = 'test-only-credential-not-a-provider-pattern'
    (tmp_path / '.env').write_text('DEEPSEEK_API=' + fake + '\n')
    (tmp_path / 'report.json.gz').write_bytes(gzip.compress(fake.encode()))
    subprocess.run(['git', 'add', 'report.json.gz'], cwd=tmp_path, check=True)
    result = subprocess.run([sys.executable, str(script)], cwd=tmp_path, capture_output=True, text=True)
    assert result.returncode == 1
    assert 'configured DeepSeek key' in result.stdout
    assert fake not in result.stdout and fake not in result.stderr
