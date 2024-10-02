# Image Analysis with Anthropic's Claude LLM
This Applied Machine Learning Prototype ("AMP") allows users to perform transcription and information extraction on images using Anthropic Claude models. The app covers a variety of use cases, including text extraction, complex document question-answering, and converting unstructured content into structured formats like JSON. The advantage of using Claude 3 over traditional OCR systems is that you can specify exactly what you want to transcribe due to Claude 3's advanced reasoning capabilities.


![](/assets/anthropic-logo.png)


## Use Cases Solved With Anthropic Vision Models

1. **Transcribing Typed Text:** Extracts typed or printed text from images into editable digital text, suitable for scanned documents or printouts.

2. **Transcribing Handwritten Text:** Converts handwritten notes into machine-readable text, aiding in digitizing personal notes or historical documents.

3. **Transcribing Forms:** Extracts data from structured forms while preserving their organization, useful for automating data entry.

4. **Complicated Document QA:** Answers questions based on the content of complex documents, suitable for contexts requiring deeper understanding.

5. **Unstructured Information → JSON:** Converts unstructured document content into a structured JSON format, ideal for turning reports or diagrams into data.

6. **User Defined:** Provides flexibility for custom prompts to process images, catering to advanced or unique use cases.


## Choose Your Claude: A Model for Every Task

Several Claude models are tested and supported:
```
claude-3-5-sonnet-20240620
claude-3-opus-20240229
claude-3-sonnet-20240229
claude-3-haiku-20240307
```
![](/assets/screenshots/claude-models.png)

**Haiku:** Anthropic's fastest model that can execute lightweight actions, with industry-leading speed. Ideal for quick tasks where time is of the essence.

**Sonnet:** The best combination of performance and speed for efficient, high-throughput tasks. Strikes a balance between speed and power, making it suitable for most general-purpose tasks.

**Opus:** Anthropic's highest-performing model, capable of handling complex analysis, longer tasks with many steps, and higher-order math and coding tasks. Best for situations where accuracy and depth are prioritized over speed.



## Deployment

### AMP Deployment Methods
There are two ways to launch this prototype on CML:

1. **From Prototype Catalog** - Navigate to the Prototype Catalog on a CML workspace, select the "Document Summarization with Gemini from Vertex AI" tile, click "Launch as Project", click "Configure Project".

2. **As ML Prototype** - In a CML workspace, click "New Project", add a Project Name, select "ML Prototype" as the Initial Setup option, copy in the [repo URL](https://github.com/cloudera/CML_AMP_Image-Analysis-with-Anthropic-Claude), click "Create Project", click "Configure Project".

### AMP Deployment
In both cases, you will need to specify the `ANTHROPIC_API_KEY` *(steps in next section on how to create this)* which enables the connection between Anthropic's API and the Application in CML.

![](/assets/screenshots/amp-setup.png)

![](/assets/screenshots/amp-build-script.png)

## Requirements

### Setup API Key with Access to Anthropic

Navigate to https://console.anthropic.com/ and sign up for an account.

![](/assets/screenshots/anthropic-setup-part1.png)

![](/assets/screenshots/anthropic-setup-part2.png)

![](/assets/screenshots/anthropic-setup-part3.png)


#### Recommended Runtime
JupyterLab - Python 3.11 - Standard - 2024.05

#### Resource Requirements
This AMP creates the following workloads with resource requirements:
- CML Session: `2 CPU, 8GB MEM`
- CML Application: `2 CPU, 8GB MEM`

#### External Resources
This AMP requires pip packages and models from huggingface. Depending on your CML networking setup, you may need to whitelist some domains:
- pypi.python.org
- pypi.org
- pythonhosted.org
- huggingface.co
Additionally, it will require access to Anthropic's Claude API. Please ensure access to Claude is whitelisted as well.

## Deploying on CML
There are two ways to launch this prototype on CML:

1. **From Prototype Catalog** - Navigate to the Prototype Catalog on a CML workspace, select the "Intelligent QA Chatbot with NiFi, Pinecone, and Llama2" tile, click "Launch as Project", click "Configure Project"

2. **As ML Prototype** - In a CML workspace, click "New Project", add a Project Name, select "ML Prototype" as the Initial Setup option, copy in the [repo URL](https://github.com/cloudera/CML_AMP_Image-Analysis-with-Anthropic-Claude), click "Create Project", click "Configure Project"


## The Fine Print

All the components of the application (knowledge base, context retrieval, prompt enhancement LLM) are running within CDF and CML. This application does not call any external model APIs nor require any additional training of an LLM. The knowledge base is generated using the user-passed sitemaps in NiFi (CDF) or Python, depending on the user preference.

IMPORTANT: Please read the following before proceeding.  This AMP includes or otherwise depends on certain third party software packages.  Information about such third party software packages are made available in the notice file associated with this AMP.  By configuring and launching this AMP, you will cause such third party software packages to be downloaded and installed into your environment, in some instances, from third parties' websites.  For each third party software package, please see the notice file and the applicable websites for more information, including the applicable license terms.

If you do not wish to download and install the third party software packages, do not configure, launch or otherwise use this AMP.  By configuring, launching or otherwise using the AMP, you acknowledge the foregoing statement and agree that Cloudera is not responsible or liable in any way for the third party software packages.


Refer to the Project **NOTICE** and **LICENSE** files in the root directory. Author: Cloudera Inc.
