from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from cortexmorph_xai.synthetic.surface_mesh import generate_surface_case, save_case


if __name__ == "__main__":
    case = generate_surface_case()
    output_path = PROJECT_ROOT / "data" / "synthetic_surface_case.json"
    save_case(case, output_path)
    print(f"Saved synthetic surface case to {output_path}")
