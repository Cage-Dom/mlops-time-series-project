import sys
from pathlib import Path

# Add project root to path
proj_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(proj_root / "src"))

from app_ui.app import app


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8050)