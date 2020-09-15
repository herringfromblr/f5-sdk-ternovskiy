"""F5 DNS Cloud Service Client"""

from f5sdk.base_clients import BaseFeatureClient

class DNSCloudServiceClient(BaseFeatureClient):
    """F5 DNS Cloud Service Client
    Attributes
    ----------
    Methods
    -------
    create()
        Refer to method documentation
    activate()
        Refer to method documentation
    validate_status()
        Refer to method documentation
    list_subs()
        Refer to method documentation
    update()
        Refer to method documentation
    delete()
        Refer to method documentation
    """

    def __init__(self, client, **kwargs):
        """Initialization

        Parameters
        ----------
        client : object
            the management client object
        **kwargs :
            optional keyword arguments
        Keyword Arguments
        -----------------
        None
        Returns
        -------
        None
        """

        super(DNSCloudServiceClient, self).__init__(
            client,
            logger_name=__name__,
            uri='/v1/svc-subscription/subscriptions'
        )

    def create(self, **kwargs):
        """Create operation
        Create DNS subscription

        Parameters
        ----------
        **kwargs :
            optional keyword arguments
        Keyword Arguments
        -----------------
        config : dict
            object containing configuration
        config_file : str
            reference to a local file containing configuration
        Returns
        -------
        dict
            the serialized REST response
        """
        return self._create(**kwargs)

    def activate(self, sub_id):
        """Activate operation
        Activate DNS subscription

        Parameters
        ----------
        sub_id: str
            DNS subscription id value

        Returns
        -------
        dict
            the serialized REST response
        """
        uri = f"/v1/svc-subscription/subscriptions/{sub_id}/activate"
        return self._make_request(uri=uri, method='POST')

    def validate_status(self, sub_id):
        """Validate operation
        Validate DNS subscription status

        Parameters
        ----------
        sub_id: str
            DNS subscription id value

        Returns
        -------
        dict
            the serialized REST response
        """
        uri = f"/v1/svc-subscription/subscriptions/{sub_id}/status"
        return self._make_request(uri=uri)

    def list_subs(self, account_id):
        """List operation
        List DNS subscription

        Parameters
        ----------
        account_id: str
            account id value

        Returns
        -------
        dict
            the serialized REST response
        """
        uri = f"/v1/svc-subscription/subscriptions?catalogId=c-aaxBJkfg8u&account_id={account_id}&service_type=adns"
        return self._make_request(uri=uri)

    def update(self, **kwargs):
        """Update operation
        Update DNS subscription

        Parameters
        ----------
        sub_id: str
            DNS subscription id value

        Returns
        -------
        dict
            the serialized REST response
        """
        sub_id = kwargs.pop('sub_id', None)
        uri = f"/v1/svc-subscription/subscriptions/{sub_id}"
        return self._make_request(uri=uri, method='PUT', **kwargs)

    def delete(self, sub_id):
        """Delete operation
        Delete DNS subscription

        Parameters
        ----------
        sub_id: str
            DNS subscription id value

        Returns
        -------
        dict
            the serialized REST response
        """
        uri = f"/v1/svc-subscription/subscriptions/{sub_id}/retire"
        return self._make_request(uri=uri, method='POST')