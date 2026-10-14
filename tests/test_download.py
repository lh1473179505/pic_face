from tests.helper import get_test_asset_url
import pic_face.choices
from pic_face.download import get_static_download_size, ping_static_url, resolve_download_url_by_provider


def _huggingface_url(base_name : str, file_name : str) -> str:
	asset_path = pic_face.choices.download_provider_set.get('huggingface').get('path')
	return 'https://huggingface.co' + asset_path.format(base_name = base_name, file_name = file_name)


def test_get_static_download_size() -> None:
	github_model_url = get_test_asset_url('models-3.0.0', 'fairface.onnx')
	huggingface_model_url = _huggingface_url('models-3.0.0', 'fairface.onnx')
	assert get_static_download_size(github_model_url) == 85170772
	assert get_static_download_size(huggingface_model_url) == 85170772
	assert get_static_download_size('invalid') == 0


def test_static_ping_url() -> None:
	assert ping_static_url('https://github.com') is True
	assert ping_static_url('https://huggingface.co') is True
	assert ping_static_url('invalid') is False


def test_resolve_download_url_by_provider() -> None:
	assert resolve_download_url_by_provider('github', 'models-3.0.0', 'fairface.onnx') == get_test_asset_url('models-3.0.0', 'fairface.onnx')
	assert resolve_download_url_by_provider('huggingface', 'models-3.0.0', 'fairface.onnx') == _huggingface_url('models-3.0.0', 'fairface.onnx')
