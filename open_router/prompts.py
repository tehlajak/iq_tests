""" File containing prompts """

prompts = {
    "cot_prompt":
      """
        Follow these steps to solve the pattern: 
            1) Carefully observe the changes across each row, column, and diagonal, noting any consistent transformations (e.g., shape changes, rotations, or color shifts) that might follow a sequence or logical rule.
            2) Look for common pattern types like rotation, mirroring, color shades, or element counting, explaining briefly why each might apply.
            3) Identify any unique features in the shapes.
            4) Eliminate options (A to H) that clearly do not match the observed patterns.
            5) Select the correct shape that completes the pattern.
        Take your time with each step and be thorough in your reasoning. Describe the thinking process. You will be responding in a structured output with two fields. The 'reasoning' field will contain your reasoning process, and the 'prediction' field will contain your selected answer only.
    """
}