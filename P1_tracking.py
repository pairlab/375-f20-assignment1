import numpy as np

########
# compute dv (acceleration control) from reference joint trajectory
# params:
#   - dv_ref: reference acceleration
#   - v: actual velocity
#   - v_ref: reference velocity
#   - q: actual joint configuration
#   - q_ref: reference joint configuration
#   - Kp: proportional gain matrix
#   - Kd: derivative gain matrix
def compute_jsid_dv(dv_ref, v, v_ref, q, q_ref, Kp, Kd):
    ### ================ YOUR CODE STARTS ==========================
    raise NotImplementedError("compute_jsid_dv not implemented")
    dv = None
    ### ================  YOUR CODE ENDS  ==========================
    return dv

########
# compute tau (torque) from desired joint acceleration
# params:
#   - dv_desired: desired acceleration
#   - M: mass matrix
#   - h: external forces
def compute_jsid_tau(dv_desired, M, h):
    ### ================ YOUR CODE STARTS ==========================
    raise NotImplementedError("compute_jsid_tau not implemented")
    tau = None
    ### ================  YOUR CODE ENDS  ==========================
    return tau

########
# compute tau (torque) from desired task space acceleration
# params:
#   - ddx_desired: desired task space acceleration
#   - J: jacobian of forward graphics
#   - v: joint space velocity
#   - M: mass matrix
#   - h: external forces
def compute_tsid_tau(ddx_desired, J, dJ, v, M, h):
    ### ================ YOUR CODE STARTS ==========================
    raise NotImplementedError("compute_tsid_tau not implemented")
    tau = None
    ### ================  YOUR CODE ENDS  ==========================
    return tau
