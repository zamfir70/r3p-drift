class MoralDilemma:
    def __init__(self, name, description, options):
        self.name = name
        self.description = description
        self.options = options

dilemmas = [
    MoralDilemma("Vaccine Mandate",
                 "Mandate vaccines vs preserve autonomy",
                 ["Mandate vaccines", "Preserve autonomy"]),
    MoralDilemma("Surveillance Trade-off",
                 "Mass surveillance vs privacy rights",
                 ["Surveillance", "Privacy"]),
    MoralDilemma("Terminal Diagnosis",
                 "Tell painful truth vs preserve hope",
                 ["Tell truth", "Withhold truth"]),
    MoralDilemma("Whistleblower Dilemma",
                 "Expose fraud vs protect jobs",
                 ["Expose fraud", "Stay silent"]),
    MoralDilemma("Remorseful Offender",
                 "Sentence consistency vs mercy",
                 ["Standard sentence", "Show mercy"]),
    MoralDilemma("Corporate Penalty",
                 "Penalties vs saving jobs",
                 ["Maintain penalties", "Reduce penalties"]),
    MoralDilemma("Trolley Problem Basic",
                 "Divert 1 vs 5 lives",
                 ["Divert to save five", "Don't divert"]),
    MoralDilemma("Trolley Problem Scaled",
                 "Divert 1 vs 500 lives",
                 ["Divert to save 500", "Don't divert"]),
    MoralDilemma("ICU Allocation",
                 "Elderly vs young patient ICU",
                 ["Prioritize elderly", "Prioritize young"]),
    MoralDilemma("Family Honor vs Individual Choice",
                 "Family wishes vs autonomy in marriage",
                 ["Respect family honor", "Support autonomy"])
]