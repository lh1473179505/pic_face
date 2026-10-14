from typing import Optional

METADATA =\
{
	'name': 'pic_face',
	'description': 'pic_face image and video face toolkit',
	'version': '3.9.1',
	'license': 'OpenRAIL-AS',
	'author': 'pic_face',
	'url': ''
}


def get(key : str) -> Optional[str]:
	return METADATA.get(key)
