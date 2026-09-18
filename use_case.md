# Use Case Diagram

```text
                 +------------------------------+
                 | Image Denoising & Restoration|
                 +------------------------------+
                    /          |          \
                   /           |           \
                  v            v            v
              Upload       Add Noise    Select Filter
                 \             |            /
                  \            |           /
                   v           v          v
                    +----------------+
                    | Process Image  |
                    +-------+--------+
                            |
                    +-------+-------+
                    |               |
                    v               v
              View Results     Evaluate Quality
                                    |
                                    v
                              Download Image

Actor: User
