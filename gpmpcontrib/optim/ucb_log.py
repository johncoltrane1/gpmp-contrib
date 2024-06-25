# --------------------------------------------------------------
# Authors: Emmanuel Vazquez <emmanuel.vazquez@centralesupelec.fr>
# Copyright (c) 2023, CentraleSupelec
# License: GPLv3 (see LICENSE)
# --------------------------------------------------------------
import gpmp.num as gnp
from gpmpcontrib import SubsetPointwiseCriterion
import scipy.stats


class UCBLOG(SubsetPointwiseCriterion):

    def __init__(self, q, *args, **kwargs):
        self.q = q
        self.alpha = scipy.stats.norm.ppf(self.q)
        super().__init__(*args, **kwargs)

    def criterion(self, zpm, zpv):
        n = self.zi.shape[0]
        d = self.xi.shape[1]
        beta_n = self.alpha + 4 * (1 + 2 * d) * gnp.log(n/self.n0)
        return - zpm - beta_n * gnp.sqrt(zpv)

