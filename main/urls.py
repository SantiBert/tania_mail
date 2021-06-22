from django.urls import path
from .views import (IndexView,
                    EventListView,
                    EventCreateView,
                    EventUpdateView,
                    EventDeleteView,
                    EventSearchView,
                    SendEmailEventView,
                    GuestsListView,
                    GuestsCreateView,
                    GuestsUpdateView,
                    GuestsDeleteView,
                    GuestsSearchView,
                    Emails_bodyCreate,
                    Emails_bodyListView,
                    Emails_bodyUpdateView,
                    Emails_bodyDeleteView,
                    Emails_bodySearchView
                    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # Ulrs events
    path('event/', EventListView.as_view(), name='eventList'),
    path('event/create/', EventCreateView.as_view(), name='eventCreate'),
    path('event/update/<slug:slug>/',
         EventUpdateView.as_view(), name='eventUpdate'),
    path('event/delete/<slug:slug>', EventDeleteView.as_view(), name='eventDelte'),
    path('event/result/', EventSearchView.as_view(), name='eventSearch'),
    path('event/sendemail/<slug:slug>/',
         SendEmailEventView.as_view(), name='eventSend'),
    # ulrs guests
    path('guests/', GuestsListView.as_view(), name='guestsList'),
    path('guests/create/', GuestsCreateView.as_view(), name='guestsCreate'),
    path('guests/update/<slug:slug>/',
         GuestsUpdateView.as_view(), name='guestsUpdate'),
    path('guests/delete/<slug:slug>',
         GuestsDeleteView.as_view(), name='guestsDelte'),
    path('guests/result/', GuestsSearchView.as_view(), name='guestsSearch'),
    # urls emil
    path('email/', Emails_bodyListView.as_view(), name='emailList'),
    path('email/create/', Emails_bodyCreate.as_view(), name='emailCreate'),
    path('email/update/<slug:slug>/',
         Emails_bodyUpdateView.as_view(), name='emailUpdate'),
    path('email/delete/<slug:slug>',
         Emails_bodyDeleteView.as_view(), name='emailDelte'),
    path('email/result', Emails_bodySearchView.as_view(), name='emailSearch')
]
