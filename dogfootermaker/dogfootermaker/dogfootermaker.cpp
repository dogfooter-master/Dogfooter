#include "dogfootermaker.h"
#include "ui_dogfootermaker.h"

DogFooterMaker::DogFooterMaker(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::DogFooterMaker)
{
    ui->setupUi(this);
}

DogFooterMaker::~DogFooterMaker()
{
    delete ui;
}
