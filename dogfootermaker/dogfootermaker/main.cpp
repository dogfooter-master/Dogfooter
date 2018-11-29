#include "dogfootermaker.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    DogFooterMaker w;
    w.show();

    return a.exec();
}
