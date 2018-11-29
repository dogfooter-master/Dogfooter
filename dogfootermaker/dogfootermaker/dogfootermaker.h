#ifndef DOGFOOTERMAKER_H
#define DOGFOOTERMAKER_H

#include <QMainWindow>

namespace Ui {
class DogFooterMaker;
}

class DogFooterMaker : public QMainWindow
{
    Q_OBJECT

public:
    explicit DogFooterMaker(QWidget *parent = nullptr);
    ~DogFooterMaker();

private:
    Ui::DogFooterMaker *ui;
};

#endif // DOGFOOTERMAKER_H
