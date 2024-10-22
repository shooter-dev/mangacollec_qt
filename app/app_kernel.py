"""Imported modules/packages"""
import time

from app.mangacollec import MangaCollec

from app.Metier.user import User
from app.IHM.views.account_page import AccountPage
from app.IHM.views.collection_page import CollectionPage
from app.IHM.views.news_page import NewsPage
from app.IHM.views.panier_page import PanierPage
from app.IHM.views.planning_page import PlanningPage
from app.IHM.views.search_page import SearchPage
from shooterQT.lib.dependency_injection.container_interface import ContainerInterface
from shooterQT.lib.kernel import Kernel
from shooterQT.lib.router.router_interface import RouterInterface
from app.IHM.views.home_page import HomePage


class AppKernel(Kernel):
    """
    AppKernel class
    """

    def start(self, router: RouterInterface):
        print('start')
        router.call("collection")


    def routing(self, router: RouterInterface):
        print('routing')
        router.add('home', HomePage)
        router.add('news', NewsPage)
        router.add('collection', CollectionPage)
        router.add('planning', PlanningPage)
        router.add('search', SearchPage)
        router.add('panier', PanierPage)
        router.add('account', AccountPage)

    def build(self, container: ContainerInterface):
        super().build(container)
        api = MangaCollec()
        container.set(MangaCollec, api)

        # self.worker_thread = WorkerThread(container)
        # #self.worker_thread.update_signal.connect(self.update_label)
        # self.worker_thread.start()  # Démarrer le thread

        time.sleep(5)

        self.chargement_donnee(api, container)

    def chargement_donnee(self, api, container):
        user = self.creat_user(api, container)
        req_news = api.get_v2_news()
        container.set_parameter("req_news", req_news)

        req_types = api.get_genres_all_v1()
        container.set_parameter("req_types", req_types)

        req_publishers = api.get_publisher_all_v2()
        container.set_parameter("req_publishers", req_publishers)

        req_recommendation = api.get_v1_recommendation()
        container.set_parameter("req_recommendation", req_recommendation)

        req_collection = api.get_v2_collection_by_username(user.username)
        container.set_parameter("req_collection", req_collection)

        req_cart = api.cart()
        container.set_parameter("req_cart", req_cart)

    def creat_user(self, api, container):
        req_user = api.me()
        user: User = User(
            id=req_user['id'],
            email=req_user['email'],
            username=req_user['username'],
            notification_email=req_user['notification_email'],
            setting_collection_order=req_user['setting_collection_order'],
            created_at=req_user['created_at'],
            confirmed_at=req_user['confirmed_at'],
            confirmation_sent_at=req_user['confirmation_sent_at'],
            unconfirmed_email=req_user['unconfirmed_email'],
            certify_adult=req_user['certify_adult'],
            possessions_count=req_user['possessions_count'],
            ad_home_banner=req_user['ad_home_banner'],
            ad_native_home_first=req_user['ad_native_home_first'],
            ad_native_planning_perso=req_user['ad_native_planning_perso'],
            is_premium=req_user['is_premium'],
            subscriptions=[]
        )
        container.set_parameter('me', user)
        return user

# class WorkerThread(QThread):
#     update_signal = pyqtSignal(int)
#
#     def __init__(self, container):
#         super().__init__()
#         self.container = container
#         self.api: MangaCollec = container.get(MangaCollec)
#
#     def run(self):
#         # Exécuter une tâche longue en arrière-plan
#         self.chargement_donnee(self.api, self.container)
