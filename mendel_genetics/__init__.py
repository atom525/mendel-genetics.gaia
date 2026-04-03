"""Mendel's laws of heredity — Gaia knowledge package."""

from gaia.lang import claim, contradiction, question, setting

# ── Settings ──
pea_model = setting(
    "Pisum sativum (garden pea) with controlled pollination. "
    "Seven traits studied: seed shape, seed colour, pod shape, pod colour, "
    "flower colour, flower position, stem height."
)
pea_model.label = "pea_model"

two_allele_model = setting(
    "Each individual carries exactly two copies of each heritable factor "
    "(one from each parent). Factors are discrete particles, not blends."
)
two_allele_model.label = "two_allele_model"

# ── Observations ──
monohybrid_3_1 = claim(
    r"F2 offspring of monohybrid crosses show dominant:recessive ratio "
    r"$\approx 3{:}1$ across all seven traits studied by Mendel (1866)."
)
monohybrid_3_1.label = "monohybrid_3_1"

dihybrid_9_3_3_1 = claim(
    r"F2 offspring of dihybrid crosses show phenotypic ratio "
    r"$\approx 9{:}3{:}3{:}1$ for independent trait combinations."
)
dihybrid_9_3_3_1.label = "dihybrid_9_3_3_1"

f1_uniformity = claim(
    "F1 generation of crosses between true-breeding parents is phenotypically "
    "uniform, expressing only the dominant trait."
)
f1_uniformity.label = "f1_uniformity"

blending_prediction = claim(
    "Blending inheritance predicts F2 offspring should show intermediate "
    "phenotypes with variance decreasing each generation — no discrete 3:1 ratio."
)
blending_prediction.label = "blending_prediction"

# ── Contradiction ──
blending_vs_mendelian = contradiction(
    blending_prediction,
    monohybrid_3_1,
    reason="Blending inheritance cannot produce discrete 3:1 ratios. "
           "The observed F2 ratio falsifies blending and supports particulate factors.",
)
blending_vs_mendelian.label = "blending_vs_mendelian"

# ── Derived claims ──
segregation_law = claim(
    r"Law of Segregation: the two alleles for a trait separate during gamete "
    r"formation so each gamete carries exactly one allele.",
    given=[monohybrid_3_1, f1_uniformity],
)
segregation_law.label = "segregation_law"

independent_assortment = claim(
    r"Law of Independent Assortment: alleles of different genes assort "
    r"independently during gamete formation.",
    given=[dihybrid_9_3_3_1, segregation_law],
)
independent_assortment.label = "independent_assortment"

particulate_inheritance = claim(
    "Hereditary information is encoded in discrete particulate factors (genes) "
    "that are transmitted unchanged between generations.",
    given=[blending_vs_mendelian, segregation_law, independent_assortment],
)
particulate_inheritance.label = "particulate_inheritance"

# ── Open question ──
linkage_question = question(
    "Do genes on the same chromosome assort independently? "
    "Morgan's linkage experiments (1910) show exceptions."
)
linkage_question.label = "linkage_question"

__all__ = [
    "monohybrid_3_1", "dihybrid_9_3_3_1", "f1_uniformity",
    "blending_prediction", "blending_vs_mendelian",
    "segregation_law", "independent_assortment", "particulate_inheritance",
]
