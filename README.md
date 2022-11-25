# Module Integration Architecture for Learning by Asking (LBA)
Multimodal time-series data-based integration architecture for recognizing and supplementing with uncertainties. This architecture contains four modules as shown in the image below.


## Module Information

- **Knowledge Module** from Hanyang University (Prof. Eun-Sol Kim)
    - Construction of neuro-symbolic knowledge graph from DramaQA dataset
    - Example of input/output
        - Input: Each frame of a video
            ```bash
            ["./dramaqa_frames/AnotherMissOh15/003/0080/IMAGE_0000008630.jpg",
             "./dramaqa_frames/AnotherMissOh15/003/0080/IMAGE_0000008574.jpg",
             ...
             "./dramaqa_frames/AnotherMissOh15/003/0080/IMAGE_0000008702.jpg"]
            ```
        - Output: Each frame of a video with detected objects and relations (predicates)
            ```bash
            ["./dramaqa_frames/AnotherMissOh15/003/0080/IMAGE_0000008630.jpg",
             "./dramaqa_frames/AnotherMissOh15/003/0080/IMAGE_0000008574.jpg",
             ...
             "./dramaqa_frames/AnotherMissOh15/003/0080/IMAGE_0000008702.jpg",
             ./dramaqa_frames/AnotherMissOh15/003/0080/custom_data_info.json,
             ./dramaqa_frames/AnotherMissOh15/003/0080/custom_prediction.json,]
            ```
            - ```custom_data_info.json``` contains classes of both objects and predicates
            - ```custom_prediction.json``` contains bounding boxes of obect, edge labels, and scores of predicted predicates
    - Repo.: https://github.com/youngyoung1021/scene_graph_extract

- **Out-of-Distribution (OOD) Detection Module** from KAIST (Prof. Chang-Dong Yoo and Prof. Junmo Kim)
    - Prof. Chang-Dong Yoo: Anserability Reasoning submodule
        - Inference of answerability reasoning from the question given an image
        - Example of input/output
        
        - Repo.: https://github.com/tomyoon2/LBA-ARVQA

    - Prof. Junmo Kim: OOD diffusion
        - Calculation of OOD diffusion score from a given image
        - Example of input/output
            - Input: Each frame of a video 
                ```bash
                {
                    "train_images": [
                        "./dramaqa_frames/AnotherMissOh15/003/0080/IMAGE_0000008630.jpg",
                        "./dramaqa_frames/AnotherMissOh15/003/0080/IMAGE_0000008574.jpg",
                        ...
                        "./dramaqa_frames/AnotherMissOh15/003/0080/IMAGE_0000008702.jpg",
                    ],
                    "test_images": [
                        "./dramaqa_frames/AnotherMissOh17/005/0085/IMAGE_0000008574.jpg"
                    ]
                }
                ```
            - Output: Score of Out-of-Distribution (OOD) diffusion
                ```bash
                {
                    "./dramaqa_frames/AnotherMissOh17/005/0085/IMAGE_0000008521.jpg": 0.7401852011680603
                }
                ```
        - Repo.: https://github.com/hushon/ood-diffusion
    
- **Question Generation Module** from Kyunghee University (Prof. Seong-Bae Park)
    - Generating (sub)-questions based on OOD information
    - Example of input/output
        - Input: 
            ```bash
            [{
                "vid" : AnotherMissOh14_001_0000,
                "False_promise" : "Haeyoung1 and Dokyung are in love and the two went through many things before starting to date."
            }]
            ```
        - Output
            ```bash
            [{"question" : "How did Haeyoung1 feel when Haeyoung1 was with Dokyung?"}]
            ```
    - Repo.: https://github.com/gminipark/LBA-DramaQG


- **Oracle Module** from Seoul National University (Prof. Byoung-Tak Zhang & Minsu Lee)
    - Take answers for (sub)-questions from oracle module & utilize answers and knowledge systems to select appropriate responses to VideoQA's questions
    - Example of input/output
        - Input: 
            ```bash
            [{"question" : "How did Haeyoung1 feel when Haeyoung1 was with Dokyung?"}]
            ```
        - Output
            ```bash
            [{"answer_from_oracle" : "Happy"}]
            ```
    - Repo.: https://github.com/greeksharifa/LBA_integration/oracle_module

---

# Installation

```bash
git clone --recurse-submodules https://github.com/greeksharifa/LBA_Integration.git

```

## Update submodules
```bash
# in root directory
git submodule update --remote scene_graph_extract
git submodule update --remote LBA-ARVQA
git submodule update --remote ood-diffusion
git submodule update --remote LBA-DramaQG
git submodule update --remote DramaQA
```
