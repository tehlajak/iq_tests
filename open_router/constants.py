prompt = "cot_prompt"
model = "google/gemini-2.0-flash-001"
dataset_type = "3_comp"
datasets = ["oa_os_oc", "oa_os_nc", "oa_ns_oc", "oa_ns_nc",
            "na_os_oc", "na_os_nc", "na_ns_oc", "na_ns_nc"
            ]

configs = ["center_single", "distribute_four", "distribute_nine",
        "in_center_single_out_center_single", "in_distribute_four_out_center_single",
        "left_center_single_right_center_single", "up_center_single_down_center_single"]

NUM_RUNS = 10
NUM_QUESTIONS = 14