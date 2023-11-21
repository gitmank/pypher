import typer
import utilities

app = typer.Typer()
decoder = typer.Typer()
encoder = typer.Typer()
app.add_typer(decoder, name="decode")
app.add_typer(encoder, name="encode")

@decoder.command()
def caesar(text: str, shift: int = None, bruteforce: bool = False):
    if(shift is None):
        typer.echo("📍 no shift provided, bruteforcing")
        bruteforce = True
    typer.echo("- decoding caesar cipher")
    if(bruteforce):
        for i in range(1, 26):
            ans = utilities.to_caesar(text, i)
            typer.echo(f"shift {i}: {ans}")
    else:
        typer.echo(utilities.from_caesar(text, -shift))

@encoder.command()
def caesar(text: str, shift: int = None):
    if(shift is None):
        typer.echo("📍 no shift provided, defaulting to 13")
        shift = 13
    typer.echo("- encoding caesar cipher")
    typer.echo(utilities.to_caesar(text, shift))

@decoder.command()
def vigenere(text: str, key: str):
    typer.echo(utilities.from_vigenere(text, key))

@encoder.command()
def vigenere(text: str, key: str):
    typer.echo(utilities.to_vigenere(text, key))

@decoder.command()
def playfair(text: str, key: str):
    typer.echo(utilities.from_playfair(text, key))

@encoder.command()
def playfair(text: str, key: str):
    typer.echo(utilities.to_playfair(text, key))

if __name__ == "__main__":
    app()

