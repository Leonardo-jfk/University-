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

        # Algoritmo 1
        if self.id_alg == 1:
            if self.monto_base <= 60000:
                porcentaje_extra = 0.0
            else:
                porcentaje_extra = self.monto_base * (digito_punto / 100.0)

            suma_fija = 0.0
            if self.complejidad == 'A' and letra != 'U':
                suma_fija = self.monto_base / 2.0

            return self.monto_base + porcentaje_extra + suma_fija

        # Algoritmo 2
        elif self.id_alg == 2:
            if 'A' <= letra <= 'P':
                porcentaje_extra = self.monto_base * (digito_punto / 100.0)
            else:
                if self.complejidad == 'A':
                    porcentaje_extra = self.monto_base * ((digito_punto * 2) / 100.0)
                else:
                    porcentaje_extra = self.monto_base * 0.15

            return self.monto_base + porcentaje_extra

        # Algoritmo 3
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

        # Cálculo normal (TP1) para cualquier otro id de algoritmo
        else:
            monto_fijo = 25000
            if 'A' <= letra <= 'L':
                monto_letra = 25000
            elif 'M' <= letra <= 'Z' and letra != 'U':
                monto_letra = 40000
            else:
                monto_letra = 100000
            porcentaje_extra = 1 + (digito_punto / 100.0)
            return (monto_fijo + monto_letra + self.monto_base) * porcentaje_extra

    def calcular_cobertura(self, afiliado):
        """Devuelve (monto_final, monto_cubierto, monto_no_cubierto, tope_aplicado).
        Si afiliado es None, el paciente no tiene obra social."""
        monto_final = self.calcular_monto_final()

        if afiliado is None:
            return monto_final, 0.0, monto_final, False

        cubierto = monto_final * porcentaje_cobertura(Afiliado.nivel, self.complejidad)
        tope_aplicado = False
        if cubierto > Afiliado.tope:
            cubierto = Afiliado.tope
            tope_aplicado = True

        return monto_final, cubierto, monto_final - cubierto, tope_aplicado


class Afiliado:
    def __init__(self, dni, obra_social, nivel, tope):
        self.dni = int(dni)
        self.obra_social = int(obra_social)
        self.nivel = int(nivel)
        self.tope = float(tope)


def porcentaje_cobertura(nivel, complejidad):
    """Tabla de porcentajes de cobertura (R = regular, A = alta complejidad)."""
    if nivel == 1:
        return 0.40 if complejidad == 'A' else 0.50
    elif nivel == 2:
        return 0.60 if complejidad == 'A' else 0.70
    else:
        return 0.80 if complejidad == 'A' else 0.90


if __name__ == "__main__":
    pass