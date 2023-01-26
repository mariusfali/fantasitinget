from verden import Verden
from politiker import Politiker
from parti import Parti
#from liga import Liga

min_verden = Verden()

for politiker in politikereliste:
    ny_politiker = Politiker(fornavn, etternavn, parti, verdi)
    min_verden.append(ny_politiker)

mitt_lag = Parti("Kulefolk")
jonas = min_verden.finn_politiker("Jonas Garh Støre")
mitt_lag.legg_til_spiller(jonas)