import streamlit as st
import base64
from gen_ai_hub.proxy.native.openai import chat

# Initialize the model name
MODEL_NAME = "gpt-4o"  # Replace with your specific model

# Function to encode image to base64
def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')

# Streamlit app
def main():
    st.title("Threat Modeling with STRIDE using LLM")

    # Step 1: Upload image
    uploaded_image = st.file_uploader("Upload your system diagram (JPEG/PNG)", type=["jpeg", "jpg", "png"])

    if uploaded_image is not None:
        # Step 2: Display uploaded image
        st.image(uploaded_image, caption="Uploaded Diagram", use_column_width=True)

        # Step 3: Encode the image to Base64
        base64_image = encode_image(uploaded_image)
        
        # Step 4: Prepare the LLM input messages
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                    "Please analyze this diagram for threat modeling. For each major component, identify specific threats using STRIDE "
                    "(Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege), providing concise explanations. "
                    "Then, suggest general mitigation strategies for each component without categorizing them under STRIDE. Additionally, identify any cross-cutting threats that "
                    "may affect multiple components (e.g., lack of logging, shared vulnerabilities, or exposure risks) and suggest mitigations for these overarching threats. "
                    "Format the output as follows:\n"
                    "- List each component.\n"
                    "- For each component, list threats under STRIDE with concise descriptions.\n"
                    "- Provide a separate, general mitigation section without repeating STRIDE categories.\n"
                    "- After analyzing individual components, include a 'Cross-Cutting Threats' section with overarching threats that span multiple components and relevant mitigations."
                )
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ]

        # Step 5: Send the request to the LLM and get the response
        try:
            response = chat.completions.create(
                model_name=MODEL_NAME,
                messages=messages
            )
            # Step 6: Display the response
            with st.spinner("Analyzing Architecture Diagram for Threat Modeling..."):
                st.subheader("Threat Modeling Analysis:")
                print(response)
                st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error processing the image: {e}")

if __name__ == "__main__":
    main()
