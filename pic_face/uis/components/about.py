from typing import Optional

import gradio

from pic_face import metadata

METADATA_BUTTON : Optional[gradio.Button] = None


def render() -> None:
	global METADATA_BUTTON

	METADATA_BUTTON = gradio.Button(
		value = metadata.get('name') + ' ' + metadata.get('version'),
		variant = 'primary'
	)
