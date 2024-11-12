from gen_ai_hub.proxy.native.openai import chat
from utils.file_processing import extract_best_practices, summary_best_practices

def send_query_to_llm(content, instruction):
    """
    Sends a query to the LLM with specific instructions and returns the response content.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": instruction},
        {"role": "user", "content": content}
    ]
    response = chat.completions.create(model_name="gpt-4o", messages=messages)
    return response.choices[0].message.content

def risk_classification(parsed_content):
    """
    Perform risk classification on the parsed content using LLM.
    """
    instruction = """
    You are an analyst. Classify the risk level of the provided tech spec and assign a risk score.
    Consider factors such as sensitivity, exposure, and potential impact.
    """
    return send_query_to_llm(parsed_content, instruction)

def perform_rra(parsed_content):
    """
    Perform a rapid risk assessment based on Mozilla's RRA guidelines.
    """
    instruction = """
    Based on Mozilla’s Rapid Risk Assessment guidelines, assess the tech spec's risk factors.
    Focus on potential threats, likelihood, and impact on assets.
    """
    return send_query_to_llm(parsed_content, instruction)

def security_review(parsed_content, best_practices):
    """
    Perform a security review by citing specific best practices where applicable from the provided documents. 
    Best practices are summarized and provided in the prompt, guiding the LLM to make specific citations.
    """
    # Summarize best practices to use in the LLM prompt
    best_practices_summary = "\n".join(
        f"{doc_name}: {summary_best_practices(practices_text)}"
        for doc_name, practices_text in best_practices.items()
    )

    # Create instruction with best practices summary for the LLM
    instruction = f"""
    Conduct a security review on the provided technical specification, focusing on areas like authentication, authorization,
    input validation, encryption, logging, monitoring, and alerting. Reference relevant best practices from the following
    documents (by document name and section). When citing, please use the document title and section only, without printing
    full text. Example format: 'Encryption Standards Best Practices Document, Section Key Management.'

    Best Practices Summary:
    {best_practices_summary}
    """

    # Query the LLM with parsed content and instruction containing best practices
    review_output = send_query_to_llm(parsed_content, instruction)
    
    # Extract citations if necessary for additional reference
    citations = extract_best_practices(parsed_content, best_practices)
    return review_output, citations

