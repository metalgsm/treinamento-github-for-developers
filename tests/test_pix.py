from decimal import Decimal
import unittest

from exercicios.pix import avaliar_pix


class AvaliarPixTests(unittest.TestCase):
    def test_aprova_transferencia_dentro_do_saldo_e_limite(self):
        self.assertEqual(
            "aprovado",
            avaliar_pix(Decimal("50.00"), Decimal("100.00"), Decimal("200.00"), Decimal("100.00")),
        )

    def test_rejeita_valor_zerado(self):
        self.assertEqual(
            "valor inválido",
            avaliar_pix(Decimal("0"), Decimal("100.00"), Decimal("200.00"), Decimal("0")),
        )

    def test_rejeita_saldo_insuficiente(self):
        self.assertEqual(
            "saldo insuficiente",
            avaliar_pix(Decimal("120.00"), Decimal("100.00"), Decimal("200.00"), Decimal("0")),
        )

    def test_rejeita_limite_diario_excedido(self):
        self.assertEqual(
            "limite diário excedido",
            avaliar_pix(Decimal("80.00"), Decimal("100.00"), Decimal("150.00"), Decimal("100.00")),
        )

    def test_aprova_quando_atinge_limite_diario_exato(self):
        self.assertEqual(
            "aprovado",
            avaliar_pix(Decimal("50.00"), Decimal("100.00"), Decimal("150.00"), Decimal("100.00")),
        )


if __name__ == "__main__":
    unittest.main()
