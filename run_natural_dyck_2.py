import click

from failBERT.eval import eval_model as eval_model_natural_dyck_2
from failBERT.train import train_model as train_model_natural_dyck_2


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--path_train",
    default="data/natural_dyck_2/natural_dyck_2_train.csv",
)
@click.option("--path_val", default="data/natural_dyck_2/natural_dyck_2_val.csv")
@click.option("--passage_column", default="modified_sentence")
@click.option("--label_column", default="label")
@click.option("--path_save_model", default="models/best_model_natural_dyck_2.pkl")
@click.option("--epochs", default=10)
@click.option("--device", default="cpu")
def train_model(
    path_train: str,
    path_val: str,
    passage_column: str,
    label_column: str,
    path_save_model: str,
    epochs: int,
    device: str,
):
    train_model_natural_dyck_2(
        path_train,
        path_val,
        passage_column,
        label_column,
        path_save_model,
        epochs,
        device,
    )


@click.command()
@click.option(
    "--path_test",
    default="data/natural_dyck_2/natural_dyck_2_test.csv",
)
@click.option("--passage_column", default="modified_sentence")
@click.option("--label_column", default="label")
@click.option("--path_model", default="models/best_model_natural_dyck_2.pkl")
@click.option("--device", default="cpu")
def eval_model(
    path_test: str,
    passage_column: str,
    label_column: str,
    path_model: str,
    device: str,
):
    eval_model_natural_dyck_2(
        path_test,
        passage_column,
        label_column,
        path_model,
        device,
    )


cli.add_command(train_model)
cli.add_command(eval_model)

if __name__ == "__main__":
    cli()
