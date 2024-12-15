import google.generativeai as genai
import gradio as gr
import tempfile
import os
import time

# Configure API key
GOOGLE_API_KEY = "api_key"
genai.configure(api_key=GOOGLE_API_KEY)

def analyze_asl_video(video_path, progress=gr.Progress()):
    if not video_path:
        return "Please upload a video.", ""

    try:
        progress(0, desc="Starting video upload...")

        # Upload video to Gemini
        video_file = genai.upload_file(path=video_path)
        progress(0.3, desc="Video uploaded, processing...")

        # Check video processing status
        processing_attempts = 0
        while video_file.state.name == "PROCESSING" and processing_attempts < 30:
            time.sleep(2)
            video_file = genai.get_file(video_file.name)
            processing_attempts += 1
            progress(0.3 + (processing_attempts / 30) * 0.4, desc="Processing video...")

        if video_file.state.name == "FAILED":
            raise ValueError("Video processing failed!")

        progress(0.7, desc="Analyzing ASL signs...")

        # Gemini model settings
        model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")
        prompt = """
        Watch this ASL video CAREFULLY and provide only the English word being demonstrated. Double-check your answer before responding to avoid mistakes.

Required response format:
Signed word: [WORD]

Note: Please ensure the video shows a single, clear ASL sign being demonstrated.

Additional guidelines:

Watch the complete video at least twice before responding
If multiple signs are shown, respond with "Multiple signs detected. Please provide a video with a single sign."
If the video is unclear or incomplete, respond with "Unable to determine sign. Please provide a clearer video."
If no ASL sign is demonstrated, respond with "No ASL sign detected in video."
If you are not 100% certain of the sign, respond with "Unable to confirm sign with certainty. Please provide another video.
        """

        response = model.generate_content(
            [video_file, prompt],
            request_options={"timeout": 300}
        )

        progress(1.0, desc="Analysis complete!")
        return response.text, "✅ Analysis completed successfully!"

    except Exception as e:
        return f"Error occurred: {str(e)}", "❌ Analysis failed"

    finally:
        try:
            if 'video_file' in locals():
                video_file.delete()
        except:
            pass

# Instructions and information
instructions = """

### Description:
This project was developed within the scope of the "Community Service Practices" course in the Department of English Language Teaching at the Faculty of Education,
with the aim of supporting the communication needs of hearing-impaired individuals.
The project aims to facilitate the English learning processes of hearing-impaired students and bridge the gap between ASL (American Sign Language) and English.

Mersin - 2024

Course Instructor: Asst. Prof. Dr. OZGE KUTLU DEMIR

### Instructions:
1. Upload an ASL (American Sign Language) video in MP4 format
2. Maximum video size: 200MB

### Limitations:
- Currently supports single word signs only
- Best results with clear, frontal views
"""

# Gradio interface with improved layout
with gr.Blocks(title="ASL Video Sign Language Analysis") as demo:
    gr.Markdown("# ASL Video Sign Language Analysis")

    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown(instructions)

        with gr.Column(scale=3):
            video_input = gr.Video(
                label="Upload ASL Video (MP4)",
                format="mp4",
                height=400
            )

            with gr.Row():
                result = gr.Textbox(
                    label="Analysis Result",
                    interactive=False
                )
                status = gr.Textbox(
                    label="Status",
                    interactive=False
                )

    analyze_btn = gr.Button("Analyze Video", variant="primary")
    analyze_btn.click(
        fn=analyze_asl_video,
        inputs=[video_input],
        outputs=[result, status]
    )

    gr.Markdown("""
    ### Tips for Best Results:
    - Ensure good lighting
    - Sign clearly and at a moderate pace
    - Keep your signing hand(s) in frame
    - Avoid busy backgrounds
    """)

# Launch the interface
demo.launch(debug=True, share=True)
