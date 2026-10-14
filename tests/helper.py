import os
import tempfile

import pic_face.choices
from pic_face.filesystem import create_directory, is_directory, is_file, remove_directory
from pic_face.types import JobStatus


def get_test_asset_url(base_name : str, file_name : str) -> str:
	asset_path = pic_face.choices.download_provider_set.get('github').get('path')
	return 'https://github.com' + asset_path.format(base_name = base_name, file_name = file_name)


def get_test_example_url(file_name : str) -> str:
	return get_test_asset_url('examples-3.0.0', file_name)


def is_test_job_file(file_path : str, job_status : JobStatus) -> bool:
	return is_file(get_test_job_file(file_path, job_status))


def get_test_job_file(file_path : str, job_status : JobStatus) -> str:
	return os.path.join(get_test_jobs_directory(), job_status, file_path)


def get_test_jobs_directory() -> str:
	return os.path.join(tempfile.gettempdir(), 'pic_face-test-jobs')


def get_test_example_file(file_path : str) -> str:
	return os.path.join(get_test_examples_directory(), file_path)


def get_test_examples_directory() -> str:
	return os.path.join(tempfile.gettempdir(), 'pic_face-test-examples')


def is_test_output_file(file_path : str) -> bool:
	return is_file(get_test_output_file(file_path))


def get_test_output_file(file_path : str) -> str:
	return os.path.join(get_test_outputs_directory(), file_path)


def get_test_outputs_directory() -> str:
	return os.path.join(tempfile.gettempdir(), 'pic_face-test-outputs')


def prepare_test_output_directory() -> bool:
	test_outputs_directory = get_test_outputs_directory()
	remove_directory(test_outputs_directory)
	create_directory(test_outputs_directory)
	return is_directory(test_outputs_directory)
