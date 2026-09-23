from decimal import Decimal


def avaliar_pix(
    valor: Decimal,
    saldo: Decimal,
    limite_diario: Decimal,
    enviado_hoje: Decimal,
) -> str:
    if valor <= 0:
        return "valor inválido"
    if valor > saldo:
        return "saldo insuficiente"
    if enviado_hoje + valor > limite_diario:
        return "limite diário excedido"
    return "aprovado"
