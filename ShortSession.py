# To create sessions of 4 minutes from the specified beggining and end
def session(beg, en):
    tb = beg  # tb is the time of beggining of the i-th session, the first session starts at the specified beggining
    te = 0  # te is the time of end of the session, it'll be 4 minutes after the tb
    ses = [];
    while (tb < en):
        te = tb + timedelta(minutes=4)
        if (te > en):  # if the time exceed the specified end, te = te
            te = en
        microses = [tb, te]  # 4 minutes session
        ses.append(
            microses)  # list of all the sessions, it's possible to access to a particular session by accessing one of the indeces of the ses
        tb = te

    return ses