# --------------------------------------------------------------
# Authors: Emmanuel Vazquez <emmanuel.vazquez@centralesupelec.fr>
# Copyright (c) 2023, CentraleSupelec
# License: GPLv3 (see LICENSE)
# --------------------------------------------------------------
import gpmp.num as gnp
from gpmpcontrib import SubsetPointwiseCriterion


class Ambiguity(SubsetPointwiseCriterion):

    def __init__(self, t, *args, **kwargs):
        self.t = t
        super().__init__(*args, **kwargs)

    def criterion(self, zpm, zpv):
        alpha = 1.96

        n = self.zi.shape[0]
        d = self.xi.shape[1]
        beta_n = alpha + 4 * (1 + 2 * d) * gnp.log(n/self.n0)

        return beta_n * gnp.sqrt(zpv) - gnp.abs(zpm - self.t)
