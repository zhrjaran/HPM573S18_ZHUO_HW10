import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov


# simulating mono therapy
# create a cohort
cohort_without = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_without = cohort_without.simulate()

# simulating combination therapy
# create a cohort
cohort_with = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)
# simulate the cohort
simOutputs_with = cohort_with.simulate()

# Problem 2: print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_without, simOutputs_with)

# Problem 3 and 4: report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_without, simOutputs_with)

# If we want the Incremental Net Monetary Benefit($) large than 0, the willingness-to-pay for one additional QALY is about 23,000$