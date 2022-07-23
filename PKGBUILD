pkgname='quickalias-git'
_pkgname='qickalias'
pkgver=r14.r97e4d25.
pkgrel=1
pkgdesc="this simple python script creates pemenant aliases so you don't have to open your shell config file"
arch=("x86_64")
url="https://github.com/dCaples/quickalias"
license=("GPL3")
provides=("quickalias")
depends=("python3")
source=("quickalias.py" "Makefile")
sha256sums=('SKIP' 'SKIP')

pkgver() {
	printf "r%s.$s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}


package() {
  sudo make DESTDIR="${pkgdir}" install
}
