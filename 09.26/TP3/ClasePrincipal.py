class Tratamiento:
    def __init__(self, dni, nombre, apellido, icd10, monto_base, complejidad, id_alg):
        self.dni = int(dni)
        self.nombre = nombre
        self.apellido = apellido
        self.icd10 = icd10
        self.monto_base = float(monto_base)
        self.complejidad = complejidad.strip().upper()
        self.id_alg = int(id_alg)

    def calcular_monto_final(self):
        # Descomponer el ICD10 para los cálculos
        letra = self.icd10[0].upper()
        partes = self.icd10.split('.')

        if len(partes) > 1:
            bloque = int(partes[0][1:])
            digito_punto = int(partes[1])
        else:
            bloque = int(self.icd10[1:])
            digito_punto = 0

        # Algoritmo 1 de cálculo del monto final
        if self.id_alg == 1:
            if self.monto_base <= 60000:
                porcentaje_extra = 0.0
            else:
                porcentaje_extra = self.monto_base * (digito_punto / 100.0)

            suma_fija = 0.0
            if self.complejidad == 'A' and letra != 'U':
                suma_fija = self.monto_base / 2.0

            return self.monto_base + porcentaje_extra + suma_fija

        # Algoritmo 2 de cálculo del monto final
        elif self.id_alg == 2:
            if 'A' <= letra <= 'P':
                porcentaje_extra = self.monto_base * (digito_punto / 100.0)
            else:
                if self.complejidad == 'A':
                    porcentaje_extra = self.monto_base * ((digito_punto * 2) / 100.0)
                else:
                    porcentaje_extra = self.monto_base * 0.15

            return self.monto_base + porcentaje_extra

        # Algoritmo 3 de cálculo del monto final
        elif self.id_alg == 3:
            monto_extra = 0.0
            if self.complejidad == 'A':
                monto_extra += self.monto_base * 0.30

            if 'A' <= letra <= 'L':
                monto_extra += 20000
            elif 'M' <= letra <= 'P':
                monto_extra += 15000 + (5000 * bloque)
            else:
                monto_extra += self.monto_base * 0.10

            if monto_extra > 60000:
                monto_extra = 60000.0

            return self.monto_base + monto_extra

        # Algoritmo Normal (del TP2)
        else:
            porcentaje_extra = self.monto_base * (digito_punto / 100.0)
            monto_final = self.monto_base + porcentaje_extra
            if self.complejidad == 'A':
                # Recargo del 5% por alta complejidad estipulado en TP2
                monto_final += monto_final * 0.05
            return monto_final


if __name__ == "__main__":
    pass