"""
Formats the Portuguese verbs queried from Wikidata using query_verbs.sparql.
"""

import collections
import os
import sys

from scribe_data.utils import export_formatted_data, load_queried_data

file_path = sys.argv[0]

verbs_list, update_data_in_use, data_path = load_queried_data(
    file_path=file_path, language="Portuguese", data_type="verbs"
)

verbs_formatted = {}

all_conjugations = [
    "presFPS",
    "presSPS",
    "presTPS",
    "presFPP",
    "presSPP",
    "presTPP",
    "perfFPS",
    "perfSPS",
    "perfTPS",
    "perfFPP",
    "perfSPP",
    "perfTPP",
    "impFPS",
    "impSPS",
    "impTPS",
    "impFPP",
    "impSPP",
    "impTPP",
    "fSimpFPS",
    "fSimpSPS",
    "fSimpTPS",
    "fSimpFPP",
    "fSimpSPP",
    "fSimpTPP",
]

for verb_vals in verbs_list:
    verbs_formatted[verb_vals["infinitive"]] = {}

    for conj in all_conjugations:
        if conj in verb_vals.keys():
            verbs_formatted[verb_vals["infinitive"]][conj] = verb_vals[conj]
        else:
            verbs_formatted[verb_vals["infinitive"]][conj] = ""

verbs_formatted = collections.OrderedDict(sorted(verbs_formatted.items()))

export_formatted_data(
    formatted_data=verbs_formatted,
    update_data_in_use=update_data_in_use,
    language="Portuguese",
    data_type="verbs",
)

os.remove(data_path)
