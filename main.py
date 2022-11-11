import argparse

import os

# Submodules (Not set yet)--------------
# from ood-diffusion (KAIST Prof. Kim)
# from LBA-DramaQG (KHU Prof. Park)
# from LBA-ARVQA (KAIST Prof. Yoo)
# --------------------------------------


from oracle_module.answerer import oracle


def main(args):
    # get ood result from the ood_module constructed by KAIST
    ood_result = get_ood_result(args)

    # get augmented question generated by DramaQG model (constructed by KHU)
    aug_question = get_aug_question(args, ood_result)

    # get answer for aug question (constructed by SNU)
    aug_answer = oracle(aug_question)


    # get original DramaQA model
    dramaqa_model = model(args)


    # Systemic flow: (written by ws)---------------------------------------------------------------------------------------------------
    # 1. OOD(Out-Of-Distribution) detection using OOD submodules from DramaQA dataset.
    #   - Reasoning output (JSON format) including keys (e.g. video_id, question, answerability, premises) from LBA-ARVQA
    #   - OOD score from ood-diffusion
    # 2. Based on reasoning output and ood scroe from both LBA-ARVQA and ood-diffusion, LBA-DramaQG submodule generates questions
    # 3. Send those generated questions to oracle_module (answerer) and get answer from it.
    # 4. Then, choose an appropriate answer for a question from VideoQA by utilizing knowledge graphs and the answer of oracle_module.
    # ---------------------------------------------------------------------------------------------------------------------------------
    # Train for DramaQA
    # Maybe model.train() goes here somewhere.
    pass

    # Inference for DramaQA
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Argparse Tutorial')
    # argument는 필요한 만큼 추가한다.
    # Maybe need output_dir, save_checkpoints, and etc.
    parser.add_argument('--data-path', type=str, help='path to DramaQA dataset')

    args = parser.parse_args()
    main(args)
