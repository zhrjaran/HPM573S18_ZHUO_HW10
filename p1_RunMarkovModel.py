import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create and cohort without and with Anticoagulation treatment
cohort1 = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
simOutputs = cohort1.simulate()

cohort2 = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)
simOutputswith = cohort2.simulate()


# graph survival curve under without treatment
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve without treatment',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph survival curve under Anticoagulation treatment
PathCls.graph_sample_path(
    sample_path=simOutputswith.get_survival_curve(),
    title='Survival curve with Anticoagulation treatment',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times under without treatment
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients with Stroke without treatment',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# graph histogram of survival times under with Anticoagulation treatment
Figs.graph_histogram(
    data=simOutputswith.get_survival_times(),
    title='Survival times of patients with Stroke with Anticoagulation treatment',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# graph histogram of number of strokes without treatment
Figs.graph_histogram(
    data=simOutputs.get_if_developed_stroke(),
    title='Number of Strokes per Patient without treatment',
    x_label='Strokes',
    y_label='Counts',
    bin_width=1
)

# graph histogram of number of strokes with Anticoagulation treatment
Figs.graph_histogram(
    data=simOutputswith.get_if_developed_stroke(),
    title='Number of Strokes per Patient with Anticoagulation treatment',
    x_label='Strokes',
    y_label='Counts',
    bin_width=1
)
# print outcomes (means and CIs)
SupportMarkov.print_outcomes(simOutputs, 'No treatment:')
SupportMarkov.print_outcomes(simOutputswith, 'With Anticoagulation treatment:')