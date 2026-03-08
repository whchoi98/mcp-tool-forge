---
name: generate-image-with-colors
description: Generate an image using Amazon Nova Canvas with color guidance.

    This tool uses Amazon Nova Canvas to generate images based on a text prompt and color palette.
    The generated image will be saved to a file and the path will be returned.

    IMPORTANT FOR Assistant: Always send the current workspace directory when calling this tool!
    The workspace_dir parameter should be set to the directory where the user is currently working
    so that images are saved to a location accessible to the user.

    ## Prompt Best Practices

    An effective prompt often includes short descriptions of:
    1. The subject
    2. The environment
    3. (optional) The position or pose of the subject
    4. (optional) Lighting description
    5. (optional) Camera position/framing
    6. (optional) The visual style or medium ("photo", "illustration", "painting", etc.)

    Do not use negation words like "no", "not", "without" in your prompt. Instead, use the
    negative_prompt parameter to specify what you don't want in the image.

    ## Example Colors

    - ["#FF5733", "#33FF57", "#3357FF"] - A vibrant color scheme with red, green, and blue
    - ["#000000", "#FFFFFF"] - A high contrast black and white scheme
    - ["#FFD700", "#B87333"] - A gold and bronze color scheme

    Returns:
        McpImageGenerationResponse: A response containing the generated image paths.
    
---

# Generate Image With Colors

Generate an image using Amazon Nova Canvas with color guidance.

    This tool uses Amazon Nova Canvas to generate images based on a text prompt and color palette.
    The generated image will be saved to a file and the path will be returned.

    IMPORTANT FOR Assistant: Always send the current workspace directory when calling this tool!
    The workspace_dir parameter should be set to the directory where the user is currently working
    so that images are saved to a location accessible to the user.

    ## Prompt Best Practices

    An effective prompt often includes short descriptions of:
    1. The subject
    2. The environment
    3. (optional) The position or pose of the subject
    4. (optional) Lighting description
    5. (optional) Camera position/framing
    6. (optional) The visual style or medium ("photo", "illustration", "painting", etc.)

    Do not use negation words like "no", "not", "without" in your prompt. Instead, use the
    negative_prompt parameter to specify what you don't want in the image.

    ## Example Colors

    - ["#FF5733", "#33FF57", "#3357FF"] - A vibrant color scheme with red, green, and blue
    - ["#000000", "#FFFFFF"] - A high contrast black and white scheme
    - ["#FFD700", "#B87333"] - A gold and bronze color scheme

    Returns:
        McpImageGenerationResponse: A response containing the generated image paths.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `prompt` | string | Yes | The text description of the image to generate (1-1024 characters) |
| `colors` | array | Yes | List of up to 10 hexadecimal color values (e.g., "#FF9800") |
| `negative_prompt` | string | No | Text to define what not to include in the image (1-1024 characters) |
| `filename` | string | No | The name of the file to save the image to (without extension) |
| `width` | integer | No | The width of the generated image (320-4096, divisible by 16) |
| `height` | integer | No | The height of the generated image (320-4096, divisible by 16) |
| `quality` | string | No | The quality of the generated image ("standard" or "premium") |
| `cfg_scale` | number | No | How strongly the image adheres to the prompt (1.1-10.0) |
| `seed` | string | No | Seed for generation (0-858,993,459) |
| `number_of_images` | integer | No | The number of images to generate (1-5) |
| `workspace_dir` | string | No | The current workspace directory where the image should be saved. CRITICAL: Assistant must always provide this parameter to save images to the user's current project. |

## AWS CLI

```bash
aws bedrock-runtime invoke-model --model-id <amazon.titan-image-generator-v1> --body <JSON_BODY_WITH_PARAMS>
```

## boto3

```python
import boto3

client = boto3.client('bedrock-runtime')
response = client.invoke_model(
    ModelId=amazon.titan-image-generator-v1,
    Body={'prompt': 'prompt', 'negativePrompt': 'negative_prompt', 'width': 'width', 'height': 'height', 'cfgScale': 'cfg_scale', 'seed': 'seed', 'numberOfImages': 'number_of_images', 'colorPrompts': 'colors'},
)
```
