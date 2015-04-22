import sys, os
sys.path.append("../core")          # files from the core 
import adfisher                     # adfisher wrapper function
import web.google_news          # interacting with Google Search
import converter.reader             # read log and create feature vectors
import analysis.statistics          # statistics for significance testing

log_file = 'log.news.suggested.txt'
query_file = 'sports-queries.txt'
usern1="anzornog"
passw1="anzor1234"
# usern1="sureshanemeth"
# passw1="suresha1234"
# usern2="lilamarchesi"
# passw2="lila1234"
# usern2="samanthakearney8"
# passw2="samanthakea1234"  oct 2 1989
# usern2="lucindecarl"
# passw2="lucinde1234"  oct 2 1989

def make_browser(unit_id, treatment_id):
#   b = web.google_news.GoogleNewsUnit(browser='firefox', log_file=log_file, unit_id=unit_id, 
#       treatment_id=treatment_id, headless=False, proxy = None)
    b = web.google_news.GoogleNewsUnit(browser='firefox', log_file=log_file, unit_id=unit_id, 
        treatment_id=treatment_id, headless=True, proxy = "proxy.pdl.cmu.edu:8080")
    return b

# Control Group treatment
def control_treatment(unit):
    unit.login(username=usern1, password=passw1)
    unit.read_articles(count=5, category="Sports", time_on_site=5)
    unit.search_and_click(query_file, clickcount=3)

# Experimental Group treatment
def exp_treatment(unit):
    unit.login(username=usern2, password=passw2)


# Measurement - Collects ads
def measurement(unit):
    unit.get_news(type='suggested', reloads=5, delay=5)


# Shuts down the browser once we are done with it.
def cleanup_browser(unit):
    unit.quit()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Load results reads the log_file, and creates feature vectors
def load_results():
    pass

def test_stat(observed_values, unit_assignments):
    pass


adfisher.do_experiment(make_unit=make_browser, treatments=[control_treatment, control_treatment], 
                        measurement=measurement, end_unit=cleanup_browser,
                        load_results=load_results, test_stat=test_stat, ml_analysis=True, 
                        num_blocks=1000, num_units=2, timeout=2000,
                        log_file=log_file, exp_flag=True, analysis_flag=False, 
                        treatment_names=["anzor-suggested"])