# ASL Video Sign Language Analysis

## About The Project

This project was developed under the auspices of the Community Service Practices course in the Department of English Language Teaching, Faculty of Education, addressing the communication needs of individuals with hearing impairments. The primary objective of this initiative is to facilitate the English language acquisition process for hearing-impaired students while establishing a comprehensive bridge between American Sign Language (ASL) and English language competencies.

Course Instructor: Asst. Prof. Dr. ÖZGE KUTLU DEMİR

### Academic and Social Contribution

The project aims to contribute in the following areas:

* Increasing access to foreign language education for hearing-impaired students
* Supporting inclusive education practices with technology
* Providing an AI-powered educational tool for sign language-English translation
* Developing special education awareness among teacher candidates
* Contributing to the academic and social development of hearing-impaired individuals

### Target Audience

* Hearing-impaired students
* English teachers and teacher candidates
* Sign language instructors
* Special education institutions
* Schools for the hearing impaired

## Features

* ASL video upload and analysis
* Real-time sign language translation
* User-friendly web interface
* MP4 video format support
* Google Gemini AI integration

### Educational Features

* Classroom-friendly interface
* Real-time translation capability
* Analysis reports for student progress tracking
* User guide for educators
* Extensive database of common ASL signs
* Visual feedback to reduce learning difficulties

## Technical Requirements & Installation

Required libraries:
`google-generativeai`
`gradio`

Installation steps:

1. Clone the repository:
`git clone https://github.com/yeneralacayir/asl-video-analysis.git`
`cd asl-video-analysis`

2. Install required libraries:
`pip install google-generativeai gradio`

3. Set up your Google API key in the code:

```python
import google.generativeai as genai
import gradio as gr
import tempfile
import os
import time
